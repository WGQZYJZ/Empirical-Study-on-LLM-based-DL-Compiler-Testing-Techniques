split_tensors  = torch.split(input_tensor, split_sizes, dim) # Split input tensor into several tensors along given dimension using torch.split
concatenated_tensor  = torch.cat([splitted_tensors[i] for i in range(len(splitted_tensors))], dim=dim) # Concatenate the split tensors along same axis using torch.cat
split_tensors  =  [torch.split(input_tensor, split_sizes, dim) for i in range(repeat)] # Split input tensor into several tensors along given dimension using torch.split repeatedly and concat them together afterwards
