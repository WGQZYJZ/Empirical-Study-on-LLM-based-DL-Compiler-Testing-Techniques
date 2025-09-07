
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = torch.full([x1.shape[0], x1.shape[1]], 1, dtype=torch.int64, device='cuda')
        v2 = convert_element_type(v1, torch.float)
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64).cuda() # input tensor with shape (batch_size, C, H, W)
x2 = torch.full([x1.shape[0], x1.shape[1]], -2, dtype=torch.int64, device='cuda') # output tensor of the model, same shape and dtype as inputs
