
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query123, key56789012):
        qk = torch.matmul(query123, key56789012)  # Compute the dot product of a query tensor and a key tensor
        inv_scale_factor = self._calc_inv_scale_factor() 
        scaled_qk = qk / float(inv_scale_factor)  # Scale the dot product by an inverse scale factor
        softmax_qk = torch.softmax(scaled_qk, dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5, training=self._isTraining()) 
        output = dropout_qk @ value34567  # Compute the dot product of a dropout tensor and another value tensor

# Initializing the model
m123 = Model()
m56789012 = Model()

