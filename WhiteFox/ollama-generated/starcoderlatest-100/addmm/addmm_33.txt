
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2):
        v1 = torch.mm(inp1, inp2)
        v2 = v1 + inp 
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(307200)  # shape (bs * nc * H * W)
x2 = torch.randn(512, 128, 49) # bs x c h w
