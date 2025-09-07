
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = torch.full([4096, 512], 1, device=x1._meta["device"])
        v2  = convert_element_type(v1, self.__output__.dtype)
        v3  = torch.cumsum(v2, 1) 
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.rand(4096, 512).to(device=x1._meta["device"], dtype=x1._meta["dtype"])
