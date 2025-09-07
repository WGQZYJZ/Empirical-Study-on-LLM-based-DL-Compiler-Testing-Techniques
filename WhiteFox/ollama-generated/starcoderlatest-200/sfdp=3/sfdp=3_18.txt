
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(64 * 64, 256)

    def forward(self, x1, x2, mask=None):
        batch_size = x1.shape[0] # number of images in the mini-batch
        query = x1.view(batch_size, -1).permute(0, 2, 1) # (batch_size, dim, num_patches * patch_height * patch_width) => (batch_size, dim, embed_dim)

        # Compute the dot product between the query and key
        qk = self.qk(x2).view(-1, batch_size, 64, 8).permute(0, 2, 3, 1).contiguous() # (embed_dim, num_patches * patch_height * patch_width, batch_size, embed_dim) => (batch_size, embed_dim, num_patches * patch_height * patch_width)
        qk = torch.matmul(query, qk)

        # Scale the dot product by the number of heads to get the scores
        scaled_qk = qk.mul(self.num_heads)

        # Apply softmax to scores to get attention probabilities for each head
        attention_probs = self._apply_attention_dropout(scaled_qk, mask=mask).softmax(dim=-1)

        # Compute the weighted sum of each head's output using the attention probabilities as weights
        context_vector = torch.matmul(attention_probs, x2) # (batch_size, embed_dim, num_patches * patch_height * patch_width) => (batch_size, embed_dim, dim)

        # Apply layer normalization to final output of model
        x1 = self._apply_layer_norm(x1, y=context_vector)
        
        return x1
class Model(torch.nn.Module):
    def __init__(self, num_patches, attention_heads=2):
        super().__init__()

        # Set the number of heads and the head dimension for each patch
        self.num_heads = 2 
        self.head_dim = 64 * 64 // 2
        
        # Create a convolutional encoder
        self.conv1 = torch.nn.Conv2d(3, self.head_dim, 1, stride=1)

        # Create two attention layers
        self.attention1 = Attention()
        self.attention2 = Attention()

    def forward(self, x1):
        # Feed the input tensor to a convolutional encoder with 8 filters and 16x16 patches
        x2 = F.relu(self.conv1(x1))

        # Apply each attention layer sequentially
        x3 = self.attention1(x1=x1, x2=x2)
        x4 = self.attention2(x1=x1, x2=x3)
        
        return x4
# Initializing the model
m = Model(num_patches=64, attention_heads=8)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
