
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.125):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, kernel_size=(1,3), stride=(1,2), padding=(0,1))
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v2 = (v1 > 0).type(torch.FloatTensor)
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3) # Apply the where function to select elements from t1 or t3 based on the mask t2
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
