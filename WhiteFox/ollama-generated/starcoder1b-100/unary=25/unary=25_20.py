
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise
        t2 = (v1 > 0).to('cuda')
        # Multiply the output of the linear transformation by the negative slope
        v2 = v1 * -0.5
        # For each element in t2, if the element is True, choose the corresponding element from t1, otherwise choose the corresponding element from t3
        v4 = torch.where(t2, v1, v2)
        return v4


# Initializing the model
m  = Model()
