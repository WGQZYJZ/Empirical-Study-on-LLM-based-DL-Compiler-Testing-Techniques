
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
        # Negative slope used for Leaky ReLU
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1)
 
        # Boolean mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        v2  = (v1 > 0).float()
 
        # Multiply the output of the convolution by a negative slope
        v3  = -v1 * self.negative_slope
 
         # Apply the where function to select elements from v1 or v3 based on the mask v2
        v4  = torch.where(v2, v1, v3)
 
        return v4


# Initializing the model with a negative slope of `-0.5` (representing the value for Leaky ReLU)
m_lr = Model(-0.5)
 
# Inputs to the model using Leaky ReLU activation function. Since the negative slope is `0.5`, the output of the first element should be equal to 0, while the third and fourth elements should be equal to `-1`. The output of this model should therefore have two zero entries (representing the values where the Boolean mask was True)
x2 = torch.tensor([[-4., -3., -2.], [-1.,  0., -5.], [ 7.,  8., 9.]])
 
__output_2__  = m_lr(x2)

