class Hyperparameters:
    env_id = "BreakoutNoFrameskip-v4" 
    exp_name = "DQN_Breakout"
    seed = 1
    torch_deterministic = True 
    capture_video = True
    save_model = True
    
    total_timesteps = 10_000_000
    learning_rate = 1e-4
    buffer_size = 400_000
    gamma = 0.95
    tau = 1
    target_network_frequency = 1000
    batch_size = 128
    start_e = 1
    end_e = 0.01
    exploration_fraction = 0.05
    learning_starts = 80_000
    train_frequency = 4