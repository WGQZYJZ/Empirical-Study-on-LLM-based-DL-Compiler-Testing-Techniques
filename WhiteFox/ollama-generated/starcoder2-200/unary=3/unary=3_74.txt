
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1  *  0.7071067811865476 # <<<------ THIS IS THE ONLY CHANGE, the 0.5 was changed to 0.7071067811865476 <<<------
        v3  = torch.erf(v2) * 0.5 # <<<------ THIS IS THE ONLY CHANGE, the 0.7071067811865476 was changed to 0.5 <<<------
        v4  = v3 +  1 # <<<------ THIS IS THE ONLY CHANGE, the 1 was added to the output of the error function
        v5  = v2 * v4 
        return v5

# Initializing the model
m  = Model()

