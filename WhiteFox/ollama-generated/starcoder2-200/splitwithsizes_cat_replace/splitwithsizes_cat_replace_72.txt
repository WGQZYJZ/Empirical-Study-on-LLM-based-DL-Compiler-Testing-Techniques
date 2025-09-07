
# Initializing the model
m  = Model()
 
# Inputs to the model
x1   = torch.randn(8, 32)
 
 # Splitting
split_sizes  = [4,4]  # The input tensor is split into two tensors of size (4,32).
 
 # Concanting along a 0-dimension
splitted_tensors  =  m.split(x1, dim=0)
 
# Initializing the model and initializing the parameters
m   =  Model()
m.init_params()
 
  # Concatenation
  concatenated_tensor = m.cat([splitted_tensors[i] for i in range(2)], dim=0)
 
  # Replacing
m  = Model()
x1  = torch.randn(8,32).to("cuda")
x2  = x1 + 2;
# Concatenating using the default concat dim and using cat 0
cat_dim   = m.default_concat_dim() # Returns -1 which means  use the default concat dimension as 0 (The concat dim in torch.nn.Linear class is 0 by default)
splitted_tensors2, splitted_tensors3  = x1.split([4] * 2), [x1 + 2 for _ in range(2)] # split into 8 tensors of size 4, 8 tensors of size 32. the split_sizes are set to 4
cat_tensors = m.cat(torch.stack([splitted_tensors2[0], x2]), dim=1) # Concatenate two tensors along dimension 1. Since the default concat dim is used here, you don't need to pass in this argument for torch.nn.Linear class (default_concat_dim function returns -1 which means use the default concat axis as 1 by default).

