
class Model(torch.nn.Module):
    def __init__(self, negative_slope=1):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.linear(x1)
        mask = (v1 > 0)  # Create a boolean tensor where each element is True if the corresponding element in v1 is greater than 0, and False otherwise
        v2 = torch.where(mask, v1, self.negative_slope * v1) # For each element in mask, if the element is True, choose the corresponding element from v1, otherwise choose the corresponding element from the multiplication by the negative slope (t3). This is essentially implementing the Leaky ReLU activation function.
        return v2


# Initializing the model
m = Model(negative_slope=0.5)


