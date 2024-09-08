from concurrent.futures import ProcessPoolExecutor, wait
from type_annotations import RedFlag
from services import (
    whataboutism_service,
    emotional_clickbait_service,
    trolling_service,
    polarization_service,
)

N_EXECUTORS: int = 4

def run_services(tweet: str) -> list:
    services = [
        whataboutism_service,
        emotional_clickbait_service,
        trolling_service,
        polarization_service,
    ]

    with ProcessPoolExecutor(N_EXECUTORS) as exe:
        futures = [
            exe.submit(service, tweet) for service in services
        ]
        wait(futures)

    results = []
    
    for f in futures:
        if f.result() is not None:
            results.extend(f.result())

    return [
        RedFlag(
            RedFlagId=result[0],
            Phrase=result[1],
            Description=result[2]
        ) for result in results
    ]
