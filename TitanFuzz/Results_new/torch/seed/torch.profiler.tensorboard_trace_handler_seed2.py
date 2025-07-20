input = torch.rand(1, 3, 224, 224)
torch.profiler.tensorboard_trace_handler('./traces', 'resnet50', True)