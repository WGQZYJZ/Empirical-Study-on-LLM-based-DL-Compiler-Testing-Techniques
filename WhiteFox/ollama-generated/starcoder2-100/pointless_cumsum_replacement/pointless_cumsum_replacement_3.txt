
class Model(torch.nn.Module):
    def __init__(self, device = torch.device("cpu")):
        super().__init__()
        self.arg0  = device
        self.arg2  = [3,4]
 
    def forward(self, x1):
        v1  = torch.full(self.arg2, 1) 
        v1  = convert_element_type(v1, dtype)
        v2  = torch.cumsum(t2, 1)
