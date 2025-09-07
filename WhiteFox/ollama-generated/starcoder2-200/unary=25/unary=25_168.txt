
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = self._activation(x1) 
        return v0

    @staticmethod
    def _activation(input):
        v3  = input > 0 # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise.
        v5  = -negative_slope 
        v6  = input * v5   # Multiply the output of the linear transformation by the negative slope.
        v7  = torch.where(v3, input, v6)    # For each element in t2, if the element is True, choose the corresponding element from t1, otherwise choose the corresponding element from t3. 
        return v7


# Initializing the model and setting the negative slope to be 0.5 by modifying the global `negative_slope` variable. Also initializing `negative_slope` to be set to 0.5 here so that the generated models are consistent with it.
negative_slope = 0.5
m2 = Model()
__output__1  = m2(x1)

