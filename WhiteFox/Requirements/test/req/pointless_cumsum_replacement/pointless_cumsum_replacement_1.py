t1 = torch.full((size1, size2), 1, device=device, dtype=dtype) # Create a full tensor with the shape (size1, size2) filled with ones, specified device and dtype
t2 = prims.convert_element_type(t1, dtype=new_dtype) # Convert the type of the tensor to the specified new dtype
t3 = torch.cumsum(t2, dim=1) # Compute the cumulative sum along dimension 1
