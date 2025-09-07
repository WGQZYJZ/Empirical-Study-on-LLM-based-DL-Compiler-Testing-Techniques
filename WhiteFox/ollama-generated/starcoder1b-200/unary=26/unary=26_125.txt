
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=(1, 5), stride=(1, 2))
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (x1 > 0).float() * negative_slope  # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        return torch.where(mask, x1, v1)


# Initializing the model
m = Model(negative_slope=0.3)


