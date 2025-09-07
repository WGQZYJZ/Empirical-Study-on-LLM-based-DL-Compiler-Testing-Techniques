
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.15):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0 
        v3  = v1 * negative_slope
        v4  = torch.where(v2, v1, v3)
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
 
 __output__  = m(x1)

# Score
- 20  points for completing the initial model. (You can ignore the `negative_slope` parameter in this question.)
- 15 points for creating a new model, and using it to infer with valid inputs.
-  8  points for each model/input pair. The maximum number of points you may earn is 3*4 = 12 (for an initial model, and three generated models).

# Submission format
A zip file containing two files: `model.py` and `input_tensor.pt`.  The file names are case sensitive.

