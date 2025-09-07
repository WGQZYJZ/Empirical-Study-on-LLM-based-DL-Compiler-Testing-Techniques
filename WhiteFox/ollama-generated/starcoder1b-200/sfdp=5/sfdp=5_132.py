
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=2, padding=0)
        self.linear = torch.nn.Linear(7 * 4 * 4, 10)
 
    def forward(self, x1):
        # Step 1: Reshape the input into batch x sequence x feature_width x feature_height
        x = x1.view(-1, 7, 4, 4).permute(2, 0, 3, 1).contiguous()  # Unsqueeze the channel dimension
        # Step 2: Apply pointwise convolutions with kernel sizes of (1, 1) to the input
        v = self.conv1(x)  # [batch x sequence x feature_width x feature_height]
        h = self.conv2(v).view(-1, 7 * 4 * 4)  # [batch x sequence x feature_width x feature_height]
        # Step 3: Compute the matrix multiplication of the output and the weight vector, then normalize it to [-1, 1] by dividing it with sqrt(num_features).
        # This ensures that the dot product between each pair of features (i.e., each filter) does not exceed 1, so that all weights have a norm of one in this layer.
        v2 = h @ x
        v2 = torch.div(v2, math.sqrt(h.size(-1)))
        # Step 4: Apply the error function to the output, scale it with sqrt(num_features) again, and add one.
        y = torch.erf(torch.mul(v2, 0.5)) + 1  # Add 1 to each element in the scaled dot product
        # Step 5: Multiply the output by the scaled dot product, and then apply dropout.
        v3 = y * x2 @ torch.div(attn_weight, math.sqrt(v.size(-1)), inplace=False)
        return v3


# Initializing the model
m = Model()

