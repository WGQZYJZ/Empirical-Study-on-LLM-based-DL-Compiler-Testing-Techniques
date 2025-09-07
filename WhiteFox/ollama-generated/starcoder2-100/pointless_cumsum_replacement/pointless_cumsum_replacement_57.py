
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        t1  = torch.full([40960], 1, dtype=torch.float32) # Create a tensor filled with the scalar value 1, with the specified dtype
        t2  = convert_element_type(t1, torch.float32)   # Convert the elements of the tensor to the specified dtype 
        t3  = torch.cumsum(t2, 1)                        # Compute the cumulative sum of the elements of the tensor along dimension 1
        return t3

# Initializing the model
m  = Model()


