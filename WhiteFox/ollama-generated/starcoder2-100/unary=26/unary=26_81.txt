
class Model(torch.nn.Module):
    def __init__(self, negative_slope = 10e-3):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.convtranspose(x1) # apply a transposed convolution to the input tensor
        mask_positive = v1 > 0 # create a mask where each element is True if the corresponding value in t1 is greater than zero, and False otherwise
        negative_slope = torch.tensor(negative_slope).to(v1.device) 
        v2 = v1 * negative_slope # multiply the output of the transposed convolution by the negative slope
        v3 = torch.where(mask_positive, v1, v2) # apply where to select elements from t1 or t3 based on the mask
        return v3

# Initializing the model