
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(torch.tensor(0., device="cuda"), requires_grad=True)
 
    def forward(self, x1, x2):
        v1  = torch.matmul(x1, x2) 
        v2 = v1 * scale_factor
        v3  = scaled_qk.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)  
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(8*720 + 15 * 96, device="cuda")
x2 = torch.randn(8*360+15*48, device="cuda")
__output__  = m(x1, x2)

