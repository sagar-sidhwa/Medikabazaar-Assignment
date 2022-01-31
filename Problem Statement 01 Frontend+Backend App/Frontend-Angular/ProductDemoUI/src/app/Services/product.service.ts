import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  geturl="http://127.0.0.1:8000/product/";
  posturl = "http://127.0.0.1:8000/product/";
  puturl = "http://127.0.0.1:8000/productdetails"
  constructor(private http:HttpClient) { }

  GetAllProducts(){
    return this.http.get(this.geturl);
  }

  CreateProduct(data:any){
    return this.http.post(this.posturl,data);
  };

  UpdateProduct(data:any,id:any){
    return this.http.put(this.puturl+"/"+id+"/",data);
  };

}



//API's

//1. Get - http://127.0.0.1:8000/product
//2. POST - http://127.0.0.1:8000/product/
//3. PUT - http://127.0.0.1:8000/productdetails/
//4. DELETE - http://127.0.0.1:8000/productdetails/6/
