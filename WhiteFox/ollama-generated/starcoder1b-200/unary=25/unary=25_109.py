
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x):
        # Apply a linear transformation to the input tensor
        v = self.linear(x)
 
        # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise
        v_gt_zero = v > 0
 
        # Multiply the output of the linear transformation by the negative slope
        v_neg_slope = v * negative_slope
 
        # For each element in t2, if the element is True, choose the corresponding element from t1, otherwise choose the corresponding element from t3
        v_where = torch.where(v_gt_zero, v, v_neg_slope)
        return v_where


# Initializing the model
m = Model()

