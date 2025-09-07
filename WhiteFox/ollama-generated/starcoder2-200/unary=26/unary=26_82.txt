
class Model(torch.nn.Module):
    def __init__(self, negative_slope = 0.1) -> None:
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.convt(x)
        v2 = (v1 > 0).to(torch.float32) # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v3 = v1 * negative_slope 
        v4 = torch.where(v2, v1, v3) 
        return v4


# Initializing the model
m = Model()
__input__ = torch.randn(1, 8, 64, 64) # The input tensor to the model should be different from that of previous examples
__output__  = m(__input__)

