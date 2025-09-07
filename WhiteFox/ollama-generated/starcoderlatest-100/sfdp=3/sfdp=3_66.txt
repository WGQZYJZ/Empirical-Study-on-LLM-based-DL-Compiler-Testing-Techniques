
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(1, 3, 64, 64)  # Shape (N, C_q, H_q, W_q) or (N, C_k, H_k, W_k), where N is the batch size, C_{q/k} are the number of channels, and H_{q/k} and W_{q/k} are the height and width of feature maps in the convolutional layers
key = torch.randn(1, 3, 64, 64)  # Shape (N, C_k, H_k, W_k), where N is the batch size, C_{q/k} are the number of channels, and H_{q/k} and W_{q/k} are the height and width of feature maps in the convolutional layers
value = torch.randn(1, 3, 64, 64)  # Shape (N, C_v, H_v, W_v), where N is the batch size, C_{v} are the number of channels, and H_{q/k} and W_{q/k} are the height and width of feature maps in the convolutional layers
