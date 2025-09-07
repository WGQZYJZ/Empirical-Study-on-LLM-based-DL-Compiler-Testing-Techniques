

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
    
    def forward(self, x1):
        v1  = self.conv(x1)
        
        # create a boolean mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        # The mask will have a shape of (v1.size()) and each element is either True or False based on the result.
        t2 = v1 > 0 
        # Multiply the output of the convolution by negative_slope
        # This operation adds negative_slope to each value in t3 if its corresponding element in t2 was true, and multiply it by a constant of 0 otherwise (multiplied by zero if False).
        t3 = v1 * (-1)
        # Apply where function on the output of the convolution or multiplication based on mask
        # This operation replaces all values that were True with negative_slope to each value in v4 for each element in the output of the convolution, and multiply it by 0 otherwise (multiplied by zero if False). 
        t4 = torch.where(t2, t1, t3)
        
        return t4


# Initializing model