
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, in_features, head_num=1, hidden_size=64):
        super().__init__()
 
        self.head_num = head_num
        self.hidden_size = hidden_size
        self.in_features // head_num

        self.linears = torch.nn.ModuleList([
            torch.nn.Linear(in_features, in_features, bias=False) for _ in range(head_num)])
 
    def forward(self, query, key):
        # Compute the multi-head dot product attention between `query` and `key`.
        # Shape: batch_size, 1, num_steps, num_heads, size_per_head
        # Shape: batch_size, num_steps, num_heads, size_per_head, input_units
        q_shape = query.shape
        q_b = q_shape[0]
        q_s = q_shape[1]
 
        k_shape = key.shape
        k_b = k_shape[0]
        k_s = k_shape[1]
 
        v_shape = self.linears[0].weight.shape
        v_b, v_d, v_s = v_shape[:3]
 
        qk = torch.einsum("bixygd, bjdgd -> biygd", query, key) / math.sqrt(v_d)  # Shape: batch_size, num_steps, num_heads, size_per_head
        qk = qk + attn_mask
 
        attention_weights = torch.softmax(qk, dim=-1)
        output = torch.einsum("bixygd, bjdgd -> bd", attention_weights, value)  # Shape: batch_size, num_steps, size_per_head
        return output

class EncoderBlock(torch.nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
 
        self.attention = MultiHeadAttention(in_features)

        # Add a feedforward layer (defined as dropout in the paper) and residual connection
        self.linears = torch.nn.Sequential(
            torch.nn.Linear(out_features * 3, out_features),
            torch.nn.BatchNorm1d(out_features),
            torch.nn.Dropout(0.5),
            torch.nn.Linear(out_features, out_features),
            torch.nn.BatchNorm1d(out_features),
        )
 
    def forward(self, x):
        # x: batch_size, input_units, num_steps
        y = self.attention(x, key=None)  # Shape: batch_size, output_units, num_steps
        z = torch.cat((x, x, y), dim=-1)
        return self.linears(z)

class Encoder(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.block0 = EncoderBlock(32, 32)
        self.block1 = EncoderBlock(64, 64)
 
    def forward(self, x):
        # Shape: batch_size, hidden_units, num_steps
        b0 = self.block0(x[:, :, :5])  # Shape: batch_size, output_units, num_steps
        y1 = torch.cat((x, x), dim=-2)  # Shape: batch_size, input_units * 3, num_steps
        y2 = self.block1(y1)  # Shape: batch_size, hidden_units, num_steps
 
        output = torch.cat((b0, y2), dim=-1)
        return output

class Model(torch.nn.Module):
    def __init__(self, in_features=64, out_features=64):
        super().__init__()
 
        self.encoder = Encoder()
 
        self.linears = torch.nn.Sequential(
            torch.nn.Linear(in_features * 3 + out_features * 2, in_features),
            torch.nn.BatchNorm1d(in_features),
            torch.nn.Dropout(0.5),
            torch.nn.Linear(in_features, in_features),
            torch.nn.BatchNorm1d(in_features),
        )
 
    def forward(self, x):
        # x: batch_size, input_units * 3, num_steps
        # Shape: batch_size, hidden_units, num_steps
        z = self.encoder(x[:, :, :5])  # Shape: batch_size, hidden_units, num_steps
 
        # Shapes of the tensors before and after `torch.cat` operation in this module.
        # batch_size: 16
        # x: (16, 32), y: (16, 64), z: (16, 96), input_tensor: (16, 256)
        cat_shapes = {
            'x': (b_size, -1, num_steps),
            'y': (b_size, in_features, num_steps),
            'z': (b_size, hidden_units, num_steps),
            'input_tensor': (b_size, 256)
        }
 
        # Embedding layers must have the same batch_size as input tensor.
        # The output of `cat` has the dimension that is greater than any in cat_shapes.
        x = torch.cat(cat_shapes['x'])
 
        y1 = torch.cat((z, - -
        self.conv5 = 