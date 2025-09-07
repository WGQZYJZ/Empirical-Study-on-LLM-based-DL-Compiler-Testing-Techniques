
class Model(torch.nn.Module):
    def __init__(self, negative_slope = 0.1):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3,8,1)
        self.negativeSlope = negative_slope

    def forward(self, x1):
        v1 = self.convT(x1)
        mask = v1 > 0
        v2 = v1 * self.negativeSlope # where(t2, t1, t3): select elements from t1 or t3 based on the mask t2 
        output  = torch.where(mask,v1,v2)
        return output

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1) # __output__ is the result of applying the model on `x1`

