
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        t1 = torch.full([x1.size()[0], 1], 1, dtype=torch.float64, layout=torch.strided, device='cuda:0')
        t2 = convert_element_type(t1, dtype)
        t3 = torch.cumsum(t2, dim=1) # Compute the cumulative sum of the elements of the tensor along dimension 1
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64).to('cuda:0')
