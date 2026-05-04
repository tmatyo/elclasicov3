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
			{schedule && schedule?.length > 0 && <Schedule data={schedule} />}
			{stats && stats?.length > 0 && <Stats data={stats} />}
			{fixtures && fixtures?.length > 0 && <Fixtures data={fixtures} />}
			{(error || !schedule && !stats && !fixtures) && <NoData />}
		</>
	);
}
