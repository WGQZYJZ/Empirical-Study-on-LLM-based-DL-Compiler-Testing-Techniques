split_tensors = torch.split(input_tensor, split_sizes, dim) # Split the input tensor into several tensors along a given dimension
concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim)  # Concatenate the split tensors along the same dimension
    torch.split(t, dim = 0) 
    x1 = cat(torch.split(x, num_splits = (len(dims)-1))) 
    split_sizes = torch.cat([v[i] for i in range(len(dims))]) # In the case when there is only one 'dim', we simply use `len(dims)`
    return x1 
    torch.split(t, dim = 0) 
    x1 = cat(torch.split(x, num_splits = (len(dims)-1))) # [B, C * T1, N]

    return x1  
