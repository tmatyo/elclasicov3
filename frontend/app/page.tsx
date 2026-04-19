import { FetchResultData } from "@/types/app";
import Schedule from "../src/components/Schedule";
import { useFetchData } from "@/src/service/fetchData";
import Fixtures from "@/src/components/Fixtures";
import Stats from "@/src/components/Stats";
import NoData from "@/src/components/NoData";

export default async function Home() {
	const { data, error } = await useFetchData<FetchResultData>();
	const { schedule, stats, fixtures } = data ?? { schedule: null, stats: null, fixtures: null };

	return (
		<>
			{schedule && <Schedule data={schedule} />}
			{stats && <Stats data={stats} />}
			{fixtures && <Fixtures data={fixtures} />}
			{error && <NoData />}
		</>
	);
}
