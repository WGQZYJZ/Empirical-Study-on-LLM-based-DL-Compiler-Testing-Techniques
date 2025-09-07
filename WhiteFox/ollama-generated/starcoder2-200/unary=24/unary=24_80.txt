
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.neg   = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).float() # This creates a boolean mask where each element is True if the corresponding element in t1 is greater than 0 and False otherwise.
        v3  = v1 * self.neg # multiply output of conv by neg_slope, note that we multiply using a tensor rather then a constant here since we want to preserve information about where the value is > 0.
        v4  = torch.where(v2, v1, v3) # This applies the where function to select elements from t1 or t3 based on the mask created by the previous step.
        return v4

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # Input tensor of size (batch_size x channel x height x width). Please use the same batch size and size as in __output__ above.

