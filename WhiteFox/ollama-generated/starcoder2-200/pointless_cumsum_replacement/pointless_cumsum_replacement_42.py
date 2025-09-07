
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
        v0  = torch.full([x2], 1, dtype=torch.float32) 
        v1  = convert_element_type(v0, torch.float64) # Convert the elements of the tensor to the specified dtype
        v2  = torch.cumsum(v1, 1) # Compute the cumulative sum of the elements of the tensor along dimension 1
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x2 = random.randint(50, 90).to_sparse().coalesce()
__output__  = m(x2)



