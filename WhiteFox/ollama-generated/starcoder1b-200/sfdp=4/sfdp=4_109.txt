
class Model(torch.nn.Module):
    def __init__(self, attn_head_num, attn_num_proj, attn_dim):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(64, 128, 3, stride=1, padding=1)
        self.fc = torch.nn.Linear(128 * 7 * 7, attn_head_num * attn_dim)
 
    def forward(self, x):
        # Reshape the batch to a linear input.
        x = x.view(-1, 3, 64, 64)
        # Perform pointwise convolutions with kernel size of 1 to the 3D input tensor.
        conv_1 = self.conv1(x)
        conv_2 = self.conv2(x)
        # Compute the dot product of the query and key.
        qk = torch.bmm(conv_1, conv_2)
        # Scale them.
        k = math.sqrt(torch.prod(torch.tensor([64], dtype=torch.float32)).to(qk.device)) * qk / k  # Note: Here we use a constant 0.7071067811865476 as the divisor in case of a division by zero.
        # Compute the softmax function of the scaled dot product, and then add the attention mask.
        # This is a key component of transformer models.
        attn_weight = torch.softmax(qk / k + 0.7071067811865476, dim=-1)
        # Compute the weighted sum of the value.
        x2 = torch.bmm(attn_weight, conv_2)  # Note: This is the same as using x2, but in the forward function.
        # Add an additional bias term to the output of linear projection.
        x3 = self.fc(torch.cat((x2, x), dim=1))  # Note: In this part, we don't need the weight of the additional bias term in forward function.
        return x3


# Initializing the model
m = Model(8, 50, 512)

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
