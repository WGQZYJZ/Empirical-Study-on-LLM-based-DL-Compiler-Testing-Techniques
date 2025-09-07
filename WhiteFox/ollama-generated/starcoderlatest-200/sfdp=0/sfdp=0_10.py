
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_heads=8):
        super().__init__()
        self.num_heads = num_heads
 
    def forward(self, query, key, value, inv_scale):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)  # Batch size x Length x Hidden x Num heads
        return output


class EncoderLayerNorm(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.hidden_layer_norm = torch.nn.LayerNorm(hidden_size, eps=1e-5)
        self.dropout = torch.nn.Dropout(0.2)
 
    def forward(self, x):
        residual = x  # Residual connection to the input layer (x -> y + z)
        output = self.hidden_layer_norm(x) # The layer normalization operation
        output = self.dropout(output) # Regular dropout operation on the hidden representation
 
        return output

class AttentionNorm(torch.nn.Module):
    def __init__(self, hidden_size, num_heads=8):
        super().__init__()
        self.multiheadattention = MultiHeadAttention(num_heads)
 
    def forward(self, query, key, value, inv_scale):
        attention_output = self.multiheadattention(query, key, value, inv_scale) # Batch size x Length x Hidden x Num heads
 
        return attention_output


class MLP(torch.nn.Module):
    def __init__(self, hidden_size=3072):
        super().__init__()
        self.fc1 = torch.nn.Linear(hidden_size, hidden_size)
        self.dropout = torch.nn.Dropout(p=0.1)
        self.fc2 = torch.nn.Linear(hidden_size, hidden_size)
 
    def forward(self, x):
        output = self.fc1(x) # Batch size x Length x Num heads
        output = self.dropout(output)
        output = torch.relu(output) # Batch size x Length x Num heads
 
        output = self.fc2(output) # Batch size x Length x Num heads
        output = self.dropout(output)
        output = torch.relu(output) # Batch size x Length x Num heads
 
        return output

class EncoderLayer(torch.nn.Module):
    def __init__(self, hidden_size=768, num_heads=12, dropout=0.1):
        super().__init__()
        self.attention_norm = AttentionNorm(hidden_size, num_heads) # Layer normalization after multi-head attention
        self.mlp = MLP(hidden_size)
 
    def forward(self, x, inv_scale, query, key, value):
        attn_output = self.attention_norm(query=query, key=key, value=value, inv_scale=inv_scale) # Batch size x Length x Hidden x Num heads
        residual = x + self.dropout(attn_output) # Residual connection to the input layer (x -> y + z)
 
        output = self.mlp(residual) # Batch size x Length x Num heads
        output = torch.relu(output)  # Batch size x Length x Num heads
        output = self.dropout(output)
 
        return output

class EncoderStack(torch.nn.Module):
    def __init__(self, num_layers=6):
        super().__init__()
        layer_sizes = [768] * (num_layers + 1)
        for i in range(len(layer_sizes)):
            if i == 0:
                self.add_module("layer%d" % (i), EncoderLayer(hidden_size=layer_sizes[i]))
            else:
                self.add_module("layer%d" % (i), EncoderLayer(
                    hidden_size=layer_sizes[i], num_heads=int(layer_sizes[i-1]/4)))
 
    def forward(self, x):
        output = [x] # List to store the intermediate values of each layer.
 
        for layer in self._modules["layer"]:
            x = layer(x)
            output.append(x)

        return output

class ScaledDotProductEncoderLayer(torch.nn.Module):
    def __init__(self, hidden_size=768, num_heads=12, dropout=0.1):
        super().__init__()
        self.attention = ScaledDotProductAttention()
        self.norm_layer_pre_attn = EncoderLayerNorm(hidden_size)
        self.norm_layer_post_attn = EncoderLayerNorm(hidden_size)
 
        self.dropout = torch.nn.Dropout(p=0.1)
 
    def forward(self, x):
        # Normalization before multi-head attention and layer normalization after each layer
        x  = self.norm_layer_pre_attn(x) # Batch size x Length x Hidden

        # Apply multi-head attention on the normalized tensor from above
        x = self.attention(query=x, key=x, value=x,
# -
def make_file(self):
      return True

