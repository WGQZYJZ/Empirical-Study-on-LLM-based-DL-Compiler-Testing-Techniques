
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, qk):
        v6 = (qk @ value).div(inv_scale_factor).softmax(dim=-1).dropout(p=dropout_p)
        return v6 @ torch.nn.functional.dropou


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(20, 3, 64, 64)
qk = torch.randn(8, 20, 64, 64)
