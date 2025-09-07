
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):

        # This is the first call to the multiplication
        v1 = torch.mm(x1[:, 0], x1[:, 3])

        # This is the second call to the multiplication with the same input tensor as argument
        v2 = torch.mm(v1 + 2 * (torch.ones_like(v1)), v1)

        # This is a third call of multiplication between the result of two matrix multiplications and another constant
        v3 = torch.mm(x1[:, 6], x1[:, 8]) - 0.7
        
        return [v1, v2, v3]

# Initializing the model
m = Model()

# Inputs to the model
__input1__, __input2__, __input3__, __input4__  = torch.randn(1, 6), \
                                                torch.randn(1, 5), \
                                                torch.randn(10, 9), \
                                                torch.randn(10, 8)

 # Adding the three arguments
__input_args__ = [__input1__, __input2__, __input3__, __input4__]

# Results of the calls to multiplication and addition
