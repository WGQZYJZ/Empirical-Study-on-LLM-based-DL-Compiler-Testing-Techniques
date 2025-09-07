
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor

        mask = (v1 > 0).type_as(v1) # Create a boolean mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        slope  = torch.full_like(v1, negative_slope) # Initialize a constant that is the same size as the output of the convolution and all elements are equal to negative_slope

        return torch.where(mask, v1, v1 * slope) # Apply the where function to select elements from v1 or v1 * slope based on the mask


# Initializing the model
m = Model()


# Inputs to the model 
x1 = torch.randn(32, 8, 64, 64)

## The input and output tensors should be different from previous 13.

# Model is new: Please check the forward function of your model and verify that the forward function works correctly on this input. (Hint: Use `torch.rand_like()` or `torch.rand()`)
assert torch.all(m(x1).shape == torch.Size([32, 8, 64, 64]))

