
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_norm_q = torch.nn.LayerNorm([768, 32]) # TODO: Implement here

    def forward(self, x1, x2):
        k = self.layer_norm_q(x1) * math.sqrt(0.0794608) + x1 # TODO: Implement here

        v = self.layer_norm_k(x2) * math.sqrt(0.0794608) + x2 # TODO: Implement here

        q  = torch.matmul(k, k.transpose(-2, -1)) # TODO: Implement here
        softmax_qk = torch.nn.functional.softmax(q / math.sqrt(self.dropout), dim=-1) # TODO: Implement here

        output = softmax_qk.matmul(v) # TODO: Implement here

        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 32, 768) # TODO: Specify a value of 768 and a shape of [1, 32, 768]
x2 = torch.randn(1, 32, 768) # TODO: Specify a value of 768 and a shape of [1, 32, 768]
