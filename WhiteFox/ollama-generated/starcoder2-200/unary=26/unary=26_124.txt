
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        mask = (v1 > 0).type(torch.bool)
        slope = negative_slope * torch.ones_like(v1)[mask]
        slope = torch.where(mask, torch.zeros_like(v1), slope) # slope: slope to multiply
        slope = slope.cuda() if use_gpu else slope  # Apply the where function to select elements from t1 or t3 based on the mask.
        slope = 0.7071067811865476 # Multiply the output of the transposed convolution by the negative slope.
        v2 = slope * v1 
        return v2

# Initializing the model