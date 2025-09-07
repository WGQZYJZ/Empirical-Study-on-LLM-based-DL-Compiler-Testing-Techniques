
class Model(torch.nn.Module):
    def __init__(self, in_features: int, out_features: int, negative_slope = 0.2):
        super().__init__()
        self.linear1 = torch.nn.Linear(in_features=in_features, out_features=out_features)
        self.relu = torch.nn.ReLU(negative_slope)
        self.linear2 = torch.nn.Linear(in_features=out_features, out_features=in_features)
 
    def forward(self, x):
        v1 = self.linear1(x)  # Apply a linear transformation to the input tensor
        v2 = v1 > 0   # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise
        v3 = v1 * negative_slope  # Multiply the output of the linear transformation by the negative slope
        v4 = torch.where(v2, v1, v3)   # For each element in t2, if the element is True, choose the corresponding element from t1, otherwise choose the corresponding element from t3
        v5 = self.relu(v4)  # Apply the ReLU function to the output of the linear transformation
        v6 = self.linear2(v5)  # Apply a second linear transformation to the output of the ReLU function
        return v6


# Initializing the model
m = Model(in_features=3, out_features=8)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
