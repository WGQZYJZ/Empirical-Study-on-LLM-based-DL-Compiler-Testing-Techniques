
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # You are not allowed to modify this function definition. If you need to add parameters, please do so as follows: def __init__(self, p):
        v1 = torch.nn.functional.linear(x1)  # Apply a linear transformation to the input tensor
        v2 = v1 > 0  # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise
        negative_slope = p
        v3 = v1 * negative_slope  # Multiply the output of the linear transformation by the negative slope
        v4 = torch.where(v2, v1, v3)  # For each element in t2, if the element is True, choose the corresponding element from t1, otherwise choose the corresponding element from t3
        return v4


# Initializing and evaluating the model