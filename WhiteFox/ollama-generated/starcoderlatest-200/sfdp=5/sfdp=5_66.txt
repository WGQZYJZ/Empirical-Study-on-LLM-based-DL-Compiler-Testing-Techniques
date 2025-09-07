
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.ffn_conv1 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
        self.ffn_conv2 = torch.nn.Conv2d(8, 32, 1, stride=1, padding=0)
 
    def forward(self, q, k, v):
        attn_weight = self._attn_conv_dot(q, k).transpose(-2, -1).reshape(*attn_weights_shape)
        output = torch.matmul(attn_weight, v) + x1
        ffn_output = self._ffn_conv_relu(output)  # [batch_size, num_head * d_model, input_length]
        ffn_output = torch.max(torch.max(ffn_output, -2), 1)[0]
        ffn_output = self._ffn_conv_relu(ffn_output)
        ffn_output = self._ffn_conv_add(ffn_output, output)
        return ffn_output
 
    def _attn_conv_dot(self, q, k):  # [batch_size, num_heads, query_length, d_k] @ [batch_size, num_heads, d_model, key_length] => [batch_size, num_heads, query_length, key_length]
        attn_weights = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(q.size(-1))  # Scale the dot product by the square root of input size
        return self._attn_conv_softmax(attn_weights)
 
    def _ffn_conv_relu(self, x):  # [batch_size, num_heads * d_model, input_length] => [batch_size, num_heads * d_model, input_length]
        ffn_output = torch.max(torch.max(x, -2), 1)[0]  # [batch_size, num_heads * d_model, input_length] => [batch_size, num_heads, d_model, input_length // heads]
        return self._ffn_conv_dropout(ffn_output)
 
    def _attn_conv_softmax(self, x):  # [batch_size, num_heads, query_length, key_length] => [batch_size, num_heads, query_length, key_length]
        ffn_output = torch.nn.Softmax(dim=-1)(x)  # Softmax along the last dimension of input tensor
        return self._attn_conv_dropout(ffn_output)
 
    def _ffn_conv_add(self, x, y):  # [batch_size, num_heads * d_model, input_length] @ [batch_size, num_heads * d_model, input_length] => [batch_size, num_heads * d_model, input_length]
        ffn_output = torch.matmul(x, torch.transpose(y, 1, -2))  # (batch_size, 16, input_length) @ (batch_size, 32, input_length) => (batch_size, 16, 32)
        return self._ffn_conv_dropout(ffn_output)
 
    def _ffn_conv_dropout(self, x):  # [batch_size, num_heads * d_model, input_length] => [batch_size, num_heads * d_model, input_length]
        ffn_output = torch.nn.Dropout2d(ffn_dropout)(x)  # Apply dropout to the output of the convolution
        return ffn_output
# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(1, 3, 64, 64)
k = torch.randn(1, 8, 64, 64)
v = torch.randn(1, 32, 64, 64)
x1 = m(q, k, v).permute(0, 2, 3, 1)

