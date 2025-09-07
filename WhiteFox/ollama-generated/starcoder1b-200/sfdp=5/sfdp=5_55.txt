
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        x0  = self.conv(x1)  # Input is already scaled and has the same shape as the output of the convolution
        x1_ = self.conv(x1).transpose(-1, -2).contiguous()  # The input tensor for the last convolution can be used to compute attention weights
        x2  = torch.matmul(x1_, x0) * math.sqrt(x1_.size(-2))  # Scale the dot product by sqrt(num_of_features) and apply softmax
        x3  = torch.exp(x2) / math.sqrt(x0.size(-1))  # Scale exp(scaled dot product) by sqrt(num_of_feature), then divide by sqrt(output_width^2 * output_height^2) to obtain a weight vector for the corresponding feature
        x4 = x3.transpose(-1, -2).contiguous().view(*x1_.shape[:-1] + (x1_.size(-2),))  # Reshape the feature vectors from the shape of (batch_size, width, height, num_of_features) to (batch_size * width * height, num_of_features)
        x5 = torch.matmul(x4, x3)  # Scale dot product by sqrt(num_of_feature^2), then add the softmax value of the weight vector for the corresponding feature (plus an attention mask) to get the output
        return x5


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
