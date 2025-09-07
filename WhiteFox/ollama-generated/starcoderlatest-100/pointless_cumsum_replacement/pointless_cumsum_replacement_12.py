
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        t1 = torch.full([x.shape[0], 3], 1, dtype=torch.int32)
        t2 = convert_element_type(t1, torch.float64)
        t3 = torch.cumsum(t2, 1) # Compute the cumulative sum of the elements of the tensor along dimension 1
        return t3


# Initializing the model
m = Model()


