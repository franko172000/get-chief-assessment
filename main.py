import uvicorn
if __name__ == "__main__":
    uvicorn.run(
        app="app:app",
        # host=config.APP_HOST,
        # port=config.APP_PORT,
        # reload=True if config.ENV != "production" else False,
        # workers=1,
    )
