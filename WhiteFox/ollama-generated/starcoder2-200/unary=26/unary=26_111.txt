
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.3):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 4, kernel_size=(17, 5))
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0 #Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v3  = v1 * -self.negative_slope 
        v4  = torch.where(v2, v1, v3) #Apply the where function to select elements from t1 or t3 based on the mask t2
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model
 x1 = torch.randn(1,8,60,52 )
 
 