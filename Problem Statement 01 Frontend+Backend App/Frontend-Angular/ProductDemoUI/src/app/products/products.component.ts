import { Component, OnInit, ViewChild } from '@angular/core';
import { ProductService } from '../Services/product.service';
import { ActivatedRoute, Router } from '@angular/router';
import {FormBuilder, FormsModule} from '@angular/forms'

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {

  products:any;
  productname:string='';
  productprice:string='';
  productquantity:string='';
  index=0;
  searchText = '';
  previous: string ='';
  @ViewChild('closebutton') closebutton: any;

  constructor(private productservice:ProductService,private route:ActivatedRoute,private router:Router) {

    productservice.GetAllProducts().subscribe((data)=> {
      this.products = data;
      this.products.reverse();
      console.log("data",data,this.products);
    }); 

  }

  ngOnInit(): void {
    this.productservice.GetAllProducts().subscribe((data)=> {
      this.products = data;
      this.products.reverse();
      console.log("data",data,this.products);
    });
  }

  Search(){
    if(this.searchText!== ""){
      let searchValue = this.searchText.toLocaleLowerCase();
     
      this.products = this.products.filter((pname:any) =>{
      return pname.productname.toLocaleLowerCase().match(searchValue);
      });
      console.log(this.products);
      }

      else {
        this.productservice.GetAllProducts().subscribe((data)=> {
          this.products = data;
          this.products.reverse();
          console.log("data",data,this.products);
        }); 
      }
  }

  NewProduct(data:any){
    console.log(data);

    this.productservice.CreateProduct(data).subscribe(result=>{
      console.log(result);

      this.productservice.GetAllProducts().subscribe((data)=> {
        this.products = data;
        this.products.reverse();
        console.log("data",data,this.products);
      });
      
    });

    this.closebutton.nativeElement.click();

  }

  EditProduct(i:any){
    console.log(i);
    this.index=i;
  }

  CancelEditProduct(){
    this.index=0;
    this.productservice.GetAllProducts().subscribe((data)=> {
      this.products = data;
      this.products.reverse();
    });
  }

  UpdateProduct(data:any,id:any){
    console.log(data,id);

    this.productservice.UpdateProduct(data,id).subscribe(result=>{
      console.log(result);

      this.productservice.GetAllProducts().subscribe((data)=> {
        this.products = data;
        this.products.reverse();
        console.log(this.products);
      });

    });

    this.index=0;

  }

}
