
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(12, 4)
        self.key = torch.nn.Linear(8, 4)
 
    def forward(self, x1, x2):
        vq = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of the query and the key
        vk = self.query(x2).contiguous().view(-1, 8)   # Compute the shape of the input tensor at position k from the view of [batch_size, sequence_length, channel]
        vk  = vk / torch.sqrt(torch.sum(vk**2, dim=-1))   # Compute the inverse square root of the value matrix, and broadcasting it to all dimensions where needed
        vs  = vq.div(vk) * math.pow(self.key(x1), 0.5)     # Scale by the inverse scale factor
        vw = math.sqrt(2.) * math.pow(math.pi, -0.5)   # Compute the square root of 2*Pi
        return vs, wv


# Initializing the model
m = Model()


