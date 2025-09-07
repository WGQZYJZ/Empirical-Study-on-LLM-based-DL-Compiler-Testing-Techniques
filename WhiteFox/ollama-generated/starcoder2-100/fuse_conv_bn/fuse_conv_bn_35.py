class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.conv3d(x1, self.linear.weight)  # Convolution layer (in eval mode tracking running statistics) 
        return v


m  = Model()

x1 = torch.randn(20, 50, 4, 7, 9).requires_grad_(True).to("cuda")

