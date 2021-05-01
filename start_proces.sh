#!/bin/bash

sudo systemctl daemon-reload
sudo systemctl stop bot
sudo systemctl daemon-reload
sudo systemctl enable bot
sudo systemctl start bot