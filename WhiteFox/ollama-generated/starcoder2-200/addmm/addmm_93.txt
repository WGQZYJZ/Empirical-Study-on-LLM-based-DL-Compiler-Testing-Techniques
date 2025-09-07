
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1=None, x2=None):
        v1 = torch.mm(x1, x2) # Matrix multiplication of two input tensors  x1 and x2
        
        # Add to the result matrix 3
        inp = torch.Tensor([
            [
                0.,   3978564.016357422
            ],
            
            [
                 -3978564.016357422,  92.593707053436
            ]
        ])
        
        v2 = v1 + inp  # Result of the matrix multiplication with the 'inp' tensor
        return v2

# Initializing the model
m  = Model()
