
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(in_features=512, out_features=768)
 
    def forward(self, x1):
        v0  = x1
        v1  = torch.nn.functional.layer_norm(v0, normalized_shape=[768])
        v3  = self.qk(x1)
        v4  = torch.nn.functional.layer_norm(v3, normalized_shape=[768])
        v5  = v1 * (2 - 0.09999999999999998) + v4 # Add  to the layer normalization output of the query
        v6  = torch.nn.functional.layer_norm(v5, normalized_shape=[768])
        v7  = self.qk(x1) * 0.2430259353137207 # Multiply the query by a constant
        v8  = torch.nn.functional.layer_norm(v7, normalized_shape=[768])
        v9  = v3 + v6 - v8 # Subtract from the layer normalization output of the query to the query of the previous block
        v10 = torch.nn.functional.dropout(x=torch.nn.functional.layer_norm(v9, normalized_shape=[768]), p=0.2)  # Apply dropout to the layer normalization output of the query added to the previous layer normalization output of the query and subtracted from it
        v14 = torch.nn.functional.softmax(self.qk(x1), dim=-1) * x1 # Compute the dot product of the layer normalization output of the query added to the previous layer normalization output of the query and subtracted from it with the query of the previous block
        v15 = torch.nn.functional.dropout(v14, p=0.2)  # Apply dropout to the dot product of the query added to the layer normalization output of the query and subtracted from it by the query of the previous block
        v19 = self.qk(x1) * (2 - 0.09999999999999998) # Multiply the query of the previous block by a constant
        v20 = torch.nn.functional.layer_norm(v15, normalized_shape=[768]) + x1 * (1 - 0.3544207074540599) # Add to the layer normalization output of the query added to the previous layer normalization output of the query and subtracted from it by the query of the previous block multiplied by a constant
        v21 = torch.nn.functional.layer_norm(v1, normalized_shape=[768]) + v5 * (1 - 0.3544207074540599) # Add to the layer normalization output of the query added to the previous layer normalization output of the query and subtracted from it multiplied by a constant
        v22 = torch.nn.functional.layer_norm(v1, normalized_shape=[768]) + (x1 * 0.5) # Add to the layer normalization output of the query added to the previous layer normalization output of the query multiplied by another constant
        v34 = x1 / v20  # Divide the layer normalization output of the query added to the previous layer normalization output of the query and subtracted from it by the query of the previous block by the dot product of the query added to the layer normalization output of the query and subtracted from it with the query of the previous block
        v40 = torch.nn.functional.softmax(self.qk(x1), dim=-1) + x1  # Compute the dot product of the layer normalization output of the query added to the previous layer normalization output of the query multiplied by another constant with the query of the previous block and add the query of the previous block
        v43 = torch.nn.functional.softmax(self.qk(x1), dim=-1) / x1  # Divide the dot product of the layer normalization output of the query added to the previous layer normalization output of the query by the query of the previous block with the layer normalization output of the query added to the previous layer normalization output of the query
        v45 = torch.nn.functional.softmax(self.qk(x1), dim=-1) / x2 # Divide the dot product of the layer normalization output of the query added to the previous layer normalization output of the query by another constant with the query of the previous block
        v68 = self.qk(v34)  + x2 * (0.95 - 1) + x1 # Add multiplied by a constant to the query of the previous block and divide it from the query of the previous block, subtract from it another constant, and divide it from another constant
        v78 = torch.nn.functional.softmax(self.qk(x1), dim=-1) / 5  # Divide the dot product of the layer normalization output of the query added to the previous layer normalization output of the query by a constant with the query of the previous block and divide it from another constant
        v79 = torch.nn.functional.softmax(self.qk(x2), dim=-1) / 6 # Divide the dot product of the layer normalization output of the query added to the previous layer normalization output of the query by a constant with another constant 
        v80 = x1 * (3 - 0.47595633770216885) + self.qk(x2) # Multiply by a constant and add multiplied by another constant to the dot product of the layer normalization output of the query added to the previous layer normalization output of the query multiplied by a constant
        v82 = torch.nn.functional.softmax(self.qk(x1), dim=-1) + 5 * x3 # Compute the dot product of the layer normalization output of the query added to the previous layer normalization output of the query and multiply it with another constant, add multiplied by a constant, and divide it from another constant
        v84 = torch.nn.functional.softmax(self.qk(x2), dim=-1) + x3 * 6 # Compute the dot product of the layer normalization output of the query added to the previous layer normalization output of the query multiplied by a constant, add multiplied by another constant, and divide it from another constant
        v85 = torch.nn.functional.softmax(self.qk(x1), dim=-1) / 6 # Divide the dot product of the layer normalization output of the query added to the previous layer normalization output of the query with another constant with a constant 
        return  v39
